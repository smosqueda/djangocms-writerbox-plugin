from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from writerbox_cms_integration.models import SectionChoicePluginModel #, WriterPluginModel, StoryPluginModel
from story.models import Story
from writer.models import Section, Writer
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils.translation import ugettext as _
import logging
logging.basicConfig(filename='/Users/smosqueda/django-playground/booger/projects/tbtdjangocms/writerbox_cms_integration/writer_cms.log',level=logging.INFO)

'''def reverse_dict(dictionary):
    reverse_dict = {}
    for key, value in dictionary.iteritems():
        if not isinstance(value, (list, tuple)):
            value = [value]
        for val in value:
            reverse_dict[val] = reverse_dict.get(val, [])
            reverse_dict[val].append(key)
    for key, value in reverse_dict.iteritems():
        if len(value) == 1:
            reverse_dict[key] = value[0]
    return reverse_dict
'''

class WriterboxPluginPublisher(CMSPluginBase):
    model = SectionChoicePluginModel  # model where plugin data are saved    
    module = _("Writerboxes")
    name = _("Writerbox Plugin")  # name of the plugin in the interface
    render_template = "writerbox_cms_integration/writerbox_plugin.html"
    logging.error("WriterboxPluginPublisher; inside publisher class")

    def render(self, context, instance, placeholder):
        #context = super(WriterboxPluginPublisher, self).render(context, instance, placeholder)
        logging.error("-----ctx= %s --------" % (instance))
        #for field in context:
        #    logging.error("field in context: %s" % field)
        #context.update({'instance': instance})
        #return context
        
        #MORE COMPLEX
        
        #context_object_name = 'list'
        one = None
        logging.error("--------IN the PLUGIN--------------")
        logging.error("----------------------")
        #def get_queryset(self):
        writer_list = None
        section_param = None
        num_param = 1
        try:
            #section_param = self.args[0].lower()
            section_param = instance 
        except:
            section_param = "news"
        logging.error("section_param %s" % (section_param))
        #try:
            #num_param = int(self.args[1])  
            #if num_param > 5: #prevent failure
            #    num_param = 3
        #except:
        #    num_param = 3
        logging.error("num_param %s" % (num_param))
        #num_param = self.args[1]
        try:
            section = get_object_or_404(Section, section_slug=section_param)
            # Get diplay count from section record in database
            num_param = section.display_count
            logging.error("got a section %s count: %s" % (section.section_slug,num_param))
            if section is not None:
                logging.error("going to build writer_list")
                writer_list = Writer.objects.filter(section__section_slug=section_param)[:num_param]
            else :
                logging.error("REALLY got NO section")
                writer_list = Writer.objects.filter(section__section_slug="news")[:num_param]
        except Exception as e:
            logging.error("EXCEPTION e: %s" % (e.message))
            section = None 

        size = len(writer_list)
        logging.error("size OF WRITER LIST is %s" % (size))
        if size < num_param:
            num_param = size
        cnt = 0
        story_list = {}
        #alt_list = {}
        writer = None
        r_story = None
        if writer_list is not None:
            logging.error("HAVE A writer_list")

            for writer in writer_list:
                one = writer_list[cnt]
                cnt += 1
                logging.error("writer: %s" % (one.name_slug))
            #logging.error("one's stuff %s %s %s" % (one.first_name, one.bio, one.section.section_slug))
                if one:
                    one_story = Story.objects.filter(section=section).filter(writers__in=[one]).order_by("-publish_date").select_related()
                    if one_story is not None:
                        r_story = one_story[0]
                        logging.error("story details: %s %s" % (r_story.headline, r_story.body_text)) 
            #writer_list = {'parrot': ('dead', 'stone'), 'lumberjack': ('sleep_all_night', 'work_all_day')}
                        key = ('key-%s' % (cnt))
                        data = (one, r_story)
                        logging.error("cnt IS %s" % (cnt))  
                        story_list[key] = data
                        logging.error("added ")
                    #if cnt == num_param:
                        #logging.error("done with list")
                        #logging.error("---------zzz-------------")
                        #break
                        #for key in story_list:
                            #pairing = story_list[key]
                            #logging.error("%s slug and story: %s" % (cnt, key)) 
                            #logging.error("%s pairing: %s %s %s" % (cnt, pairing[0].last_name, pairing[1].headline, pairing[1].body_text))
                        #logging.error("----------zzz------------")
                        #break
                    else:
                        logging.error("don't have one_story")
                        break
                else:
                    logging.error("don't have another Writer")
                    break

            #return writer_list
        else:
            logging.error("no writer_list")
            story_list = None
            #return None
        
        #if story_list is not None:
        #    instance = reverse_dict(story_list)
        #else :
        instance = story_list            
        
        context.update({'instance': instance})
        return context
        #return render(request, render_template, {'list': story_list })
        #context_object_name = 'list'
        #instance = story_list
        #context.update({'instance': instance})
        #return context
        
        

plugin_pool.register_plugin(WriterboxPluginPublisher)  # register the plugin

'''
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class WriterApphook(CMSApp):
    app_name = "writer"
    name = _("Writers Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["writer.urls"]


apphook_pool.register(WriterApphook)  # register the application

'''
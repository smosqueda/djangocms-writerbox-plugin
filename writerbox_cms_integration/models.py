from django.db import models
from cms.models import CMSPlugin
from writer.models import Section

class SectionChoicePluginModel(CMSPlugin):
    section = models.ForeignKey(Section)

    def __unicode__(self):
        return self.section.section_slug
        
'''class StoryPluginModel(CMSPlugin):
    story = models.ForeignKey(Story)

    def __unicode__(self):
        return self.headline

class SectionPluginModel(CMSPlugin):
    section = models.ForeignKey(Section)

    def __unicode__(self):
        return self.section
        #return self.section.section
    
class WriterPluginModel(CMSPlugin):
    writer = models.ForeignKey(Writer)

    def __unicode__(self):
        return self.writer
'''
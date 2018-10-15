
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class PostDeleteModelExtra(ModelExtra):
    def get_name(cls):
        return 'post_delete'
    

class PostDeleteModelExtraParserListener(BaseListener):

    def enterAn_post_delete(self, ctx: ZmeiLangParser.An_post_deleteContext):
        self.collection_set.extras.append(
            PostDeleteModelExtra(self.model)
        )

        self.model.signal_handlers.append(
            (['django.db.models.signals', 'post_delete'], self._get_code(ctx.python_code())))


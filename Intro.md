Todo vídeo deve ter uma introdução anterior ao conteúdo em si, para reforçar a identidade do GAP e dar os devidos créditos aos monitores responsáveis pela produção do vídeo.
```
from manim import *

class Intro(Scene):
    def construct(self):
        logo = ImageMobject('logo_gap.png').scale(1.5)
        self.play(FadeIn(logo, scale=0.75))
        self.wait()
```
O parâmetro em `self.wait()` diz respeito ao tempo em que a logo estará na tela, logo, deve ser levado em conta o tempo em que o monitor está apresentando o GAP e a si mesmo.\
__Obs:__ A imagem `.png` da logo pode ser obtida no drive do GAP.

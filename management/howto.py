from pathlib import Path

from jinja2 import Environment, FileSystemLoader

CURRENT_DIR = Path(__file__).parent
PROJECT_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = CURRENT_DIR / 'templates'
SOURCE_TEMPLATE = 'howto.tmpl.md'
RENDERED_TEMPLATE = 'howto.md'


env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(SOURCE_TEMPLATE)

for ut in PROJECT_DIR.glob('ut*'):
    for pop in ut.glob('pop*'):
        output = pop / RENDERED_TEMPLATE
        output.write_text(template.render(ut=ut.name, pop=pop.name))
        print(f'✔ Expanded howto.md for {pop}')

"""Generate upload-oriented text files from the modular sources; no independent edits."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'chat'
GUIDE=['Authoring-Prompt.md','World-Template.json','reference/Evidence.md','reference/Craft.md','reference/Trackers.md','reference/Triggers.md','reference/Schema.md','reference/PawScript.md','reference/Capabilities.md','reference/Recipes.md','reference/Import-Integrity.md','reference/Known-Limits.md','reference/Default-Evaluation.txt','reference/Current-AI-Profiles.json']
GROUPS={
 'IW-Authoring-Guide.txt':GUIDE,
 'IW-Examples.txt':['examples/README.md','examples/Payloads.md','examples/index.json','examples/narrative-last-ferry.json','examples/recipe-request-commit.json','examples/recipe-choice-followup.json','examples/recipe-threshold-unlock.json','examples/optional-block.json','examples/showcase-glass-ledger.json','examples/character-starting-values.json'],
 'IW-Sample-Library.txt':['library/Integration.md','library/Sample-Blocks.json']}

def build():
 OUT.mkdir(exist_ok=True);manifest={}
 for name,files in GROUPS.items():
  intro='Infinite Worlds Authoring Kit: generated text edition. Source paths below identify sections within this upload. This is reference material, not one JSON world to import. The Examples edition includes all native payload snippets plus selected complete recipes; other complete worlds remain in the full kit and can be requested by path. Follow Authoring-Prompt.md for the authoring task. Load referenced material selectively; ask for a missing companion when required. Do not claim the Python validator ran unless actual execution tools and the full tools folder are available.\n\n'
  parts=[intro]
  for path in files:
   content=(ROOT/path).read_text(encoding='utf-8')
   parts.extend(['\n===== BEGIN FILE: '+path+' =====\n',content,'\n===== END FILE: '+path+' =====\n'])
  text=''.join(parts);(OUT/name).write_text(text,encoding='utf-8')
  manifest[name]={'sourceFiles':files,'sha256':hashlib.sha256(text.encode('utf-8')).hexdigest()}
 (OUT/'sources.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
 print('Generated '+', '.join(GROUPS))
if __name__=='__main__':build()

# JustOrthologs-master/QfO_release_2022_02/Bacteria/UP000000425_122586_DNA.fasta

# /Users/bensilke/gavins-lab/notJustOrthologs/JustOrthologs-master/QfO_release_2022_02/Bacteria/UP000000425_122586_DNA.fasta
# /Users/bensilke/gavins-lab/notJustOrthologs/JustOrthologs-master/QfO_release_2022_02/Bacteria/UP000000425_85962_DNA.fasta

a = [
    "UP000000557_251221_DNA.fasta",
    "UP000001425_1111708_DNA.fasta",
    "UP000002521_190304_DNA.fasta",
    "UP000001570_224308_DNA.fasta",
    "UP000001584_83332_DNA.fasta",
    "UP000000431_272561_DNA.fasta",
    "UP000001414_226186_DNA.fasta",
    "UP000002438_208964_DNA.fasta",
    "UP000000425_122586_DNA.fasta",
    "UP000000429_85962_DNA.fasta",
    "UP000002524_243230_DNA.fasta",
    "UP000001973_100226_DNA.fasta",
    "UP000002008_324602_DNA.fasta",
    "UP000000798_224324_DNA.fasta",
    "UP000000807_243273_DNA.fasta",
    "UP000000625_83333_DNA.fasta",
    "UP000001025_243090_DNA.fasta",
    "UP000008183_243274_DNA.fasta",
    "UP000007719_515635_DNA.fasta",
    "UP000000577_243231_DNA.fasta",
    "UP000002526_224911_DNA.fasta",
    "UP000001408_189518_DNA.fasta",
    "UP000000718_289376_DNA.fasta",
]

"QfO_release_2022_02/Bacteria/UP000000557_251221_DNA.fasta"
"QfO_release_2022_02/Bacteria/UP000001425_1111708_DNA.fasta"

import os


files = [f.replace('_DNA.fasta','') for f in os.listdir('Bacteria') if '_DNA.fasta' in f]
f_text = '('
for file in files:
    f_text = f_text+file+' '
print(f_text)
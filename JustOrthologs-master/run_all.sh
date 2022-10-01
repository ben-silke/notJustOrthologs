
Raw Blame

 
#!/bin/bash
# NC_015733
# this list of ids should work for every soil reference genome
files=(UP000000557_251221 UP000001425_1111708 UP000002521_190304 UP000001570_224308 UP000001584_83332 UP000000431_272561 UP000001414_226186 UP000002438_208964 UP000000425_122586 UP000000429_85962 UP000002524_243230 UP000001973_100226 UP000002008_324602 UP000000798_224324 UP000000807_243273 UP000000625_83333 UP000001025_243090 UP000008183_243274 UP000007719_515635 UP000000577_243231 UP000002526_224911 UP000001408_189518 UP000000718_289376)
echo ${ids[@]}
folder=QfO_release_2022_02/Bacteria
ext=_DNA.fasta

# change this depending on the input
for file in "${files[@]}"
do
    echo $file
    for file_two in "${files[@]}"
    do
    echo $file_two
    if [[ "$file" == "$file_two" ]]; then
    # double chekc these labels
        echo "files are equal"
    else
        echo $file
        echo $file_two
        # python3 $just_ortho_dir -q $folder/$file -s $folder/$file_two -o testing/data/output/justorthologs/orthologs.$file.$file_two.txt -c -t 16
        time python3 $just_ortho_dir -q $folder/$file$ext -s $folder/$file_two$ext -o outputDir/$file.$file_two.output.txt -c -t 16
    fi
    done
    # strace -o data/justorthologs/trace_data/$id.txt -c -tt ____command_goes_here____
    # python script to compare the sequences.
done
# this needs to recursively loop
# Can use trace to track how long the processes take
# ben@ben-amd:~/research/biol3209/prodigal_testing$ strace -o trace -c -Ttt ./pipeline.sh
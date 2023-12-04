#! /usr/bin/env python
"""
Retrieves sequences with no annotated exceptions.
Also retrieves the longest isoform for each gene.
"""
import sys
import argparse
import gzip

# from multiprocessing import Process, current_process, freeze_support, Pool
# Multiproccessing is not necessary because the program is fast.
# However, if it were to be implemented, the commented out lines would probably be necessary.


def parseArgs():
    """
    Parses arguments. An input fasta file is required.
    The number of cores is optional. By default, all available threads are used.
    An output file is optional. If an output file is not specified, output will be writted to standard out.
    """
    import os

    parser = argparse.ArgumentParser(description="Find Orthologs in Two Files.")
    parser.add_argument(
        "-i", help="Input FASTA file", action="store", dest="input", required=True
    )
    parser.add_argument(
        "-o", help="Output FASTA File", action="store", dest="output", required=False
    )
    # parser.add_argument("-t",help="Number of Cores",action="store",dest="threads",type=int, default=-1, required=False)
    args = parser.parse_args()
    if not os.path.isfile(args.input):
        print((args.input, "is not a correct file path!"))
        sys.exit()
    return args


def writeGoodLines(args):
    """
    Input: System arguments with input and output files
    Writes fasta sequence lines that pass the filters and are the longest isoform to the output file (or standard out)
    """
    input = ""
    if args.input[-3:] == ".gz":
        input = gzip.open(args.input, "r")
    else:
        input = open(args.input, "r")
    output = open(args.output, "w") if args.output else sys.stdout
    header = ""
    geneName = ""
    countTotal = 0
    goodHeader = False
    bestGenes = dict()
    for line in input:
        line = line.strip()
        if goodHeader:
            if "Error" in line:
                goodHeader = False
                continue
            else:
                countTotal += 1
                if geneName in bestGenes:
                    if len(bestGenes[geneName][1]) < len(line):
                        bestGenes[geneName][0] = header
                        bestGenes[geneName][1] = line
                else:
                    bestGenes[geneName] = [header, line]
                header = ""
                if countTotal == 1:
                    goodHeader = False
                    countTotal = 0
        elif line[0] == ">":
            if "exception" in line:
                continue
            if "transl_except" in line:
                continue
            if "partial=true" in line:
                continue
            geneName = line.split("gene=")[1].split(";")[0] if "gene=" in line else line
            header = line
            goodHeader = True
            countTotal = 0

    for value in bestGenes.values():
        for line in value:
            output.write(line + "\n")
    input.close()
    output.close()


if __name__ == "__main__":
    """
    Main
    """
    # freeze_support()
    args = parseArgs()
    writeGoodLines(args)

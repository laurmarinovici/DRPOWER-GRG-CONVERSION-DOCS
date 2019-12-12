"""
.. module:: psse2grg

    :platform: Unix, Windows

    :synopsis: This module acts as the main script to convert an input model in PSSE format (.raw) to GRG format (.json) or vice-versa.

.. moduleauthor:: Laurentiu.Marinovici@pnnl.gov (Pacific Northwest National Laboratory)
"""

import os, sys, pytest, getopt, functools, json
import grg_grgdata, grg_psse2grg
#, grg_pssedata

print_err = functools.partial(print, file = sys.stderr)

def main(argv):
  """Main function of the module.
        
        Parameters
        ----------
        argv :
            Command line arguments given as:
            -s <source model file path> -t <output model file path>
            
        Returns
        -------
        None
        
        """
  try:
    opts, args = getopt.getopt(argv, "hs:t:", ["help", "source=", "target="])
    if not opts:
      print("ERROR: need options and arguments to run.")
      print("Usage: python psse2grg.py -s <source file to be translated (either .raw or .json)> -t <target file to save the translated data (either .json or .raw)>")
      sys.exit()
  except getopt.GetoptError:
    print("Wrong option or no input argument! Usage: python psse2grg.py -s <source file to be translated (either .raw or .json)> -t <target file to save the translated data (either .json or .raw)>")
    sys.exit(2)
  for opt, arg in opts:
    if  opt in ("-h", "--help"):
      print("Help prompt. Usage: python psse2grg.py -s <source file to be translated (either .raw or .json)> -t <target file to save the translated data (either .json or .raw)>>")
      sys.exit()
    # Set the source file for translation
    elif opt in ("-s", "--source"):
      sourceFile = arg
    # Set the source target for translation
    elif opt in ("-t", "--target"):
      targetFile = arg
  
  currFolder = os.path.dirname(os.path.realpath(__file__))
  absSource = os.path.abspath(os.path.normpath(sourceFile))
  absTarget = os.path.abspath(os.path.normpath(targetFile))
  
  if sourceFile.endswith('.raw') and targetFile.endswith('.json'):
    caseName = os.path.split(sourceFile)[1].split('.')[0]
    psseCase = grg_psse2grg.io.parse_psse_case_file(absSource)
    # psseCase = grg_pssedata.io.parse_psse_case_file(absSource)
    print('Going to convert PSSE {0:s} to GRG.'.format(caseName))
    grgData = psseCase.to_grg(caseName)
    output_file = open(absTarget, 'w')
    output_file.write(json.dumps(grgData, sort_keys=True, indent=2, \
                         separators=(',', ': ')))
    output_file.close()
    print('=============== DONE ===========')
  elif sourceFile.endswith('.json') and targetFile.endswith('.raw'):
    caseName = os.path.split(sourceFile)[1].split('.')[0]
    grgData = grg_psse2grg.io.parse_grg_case_file(absSource)
    print(json.dumps(grgData, sort_keys = True, indent = 2))
    case = grg_psse2grg.io.build_psse_case(grgData, 'starting_points', 'breakers_assignment')
    print('Going to convert GRG {0:s} to RAW.'.format(caseName))
    psseCase = case.to_psse()
    output_file = open(absTarget, 'w')
    output_file.write(psseCase)
    output_file.close()
    print('=============== DONE ===========')
    # write_mp_case exists in grg_mpdata.io, but not in grg_mp2grg.io
    #grg_mpdata.io.write_mp_case_file(absTarget, case)
  else:
    print_err('This tool does not recognize the resource and/or target file extensions as correct.')

if __name__ == '__main__':
  import sys
  main(sys.argv[1:]) 


# will terminate the program and supply the given message
raise SystemExit('It failed!')

# extra steps not necessary
import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)
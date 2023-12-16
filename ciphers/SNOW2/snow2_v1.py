# Created on Sep 2, 2020
# author: Hosein Hadipour
# contact: hsn.hadipour@gmail.com

import os

output_dir = os.path.curdir

def zsnow2(T=12):
    cipher_name = 'zsnow2'
    recommended_mg = 9
    recommended_ms = 12
    eqs = '#%s %d Rounds\n' % (cipher_name, T)
    eqs += 'connection relations\n'
    for t in range(T):
        # feedback relation
        eqs += 'S_%d, S_%d, S_%d, S_%d\n' % (t + 16, t + 11, t + 2, t)
        eqs += 'R_%d, S_%d, R_%d\n' % (t + 2, t + 5, t)  # fsm relation
        # output relation
        eqs += 'S_%d, R_%d, R_%d, S_%d, Z_%d\n' % (t + 15, t + 1, t, t, t)
    eqs += 'known\n' + '\n'.join(['Z_%d' % i for i in range(0, T - 1)])
    eqs += '\nend'
    eqsfile_path = os.path.join(output_dir, 'relationfile_%s_%dclk_mg%d_ms%d.txt' % (cipher_name, T, recommended_mg, recommended_ms))
    with open(eqsfile_path, 'w') as relation_file:
        relation_file.write(eqs)

def main():
    zsnow2(T=13)

if __name__ == '__main__':
    main()

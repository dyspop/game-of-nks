"""NKS objects."""
from random import randint
from time import sleep

def graph(
    seq=[randint(0,1) for x in range(256)],
    rule=''.join([str(randint(0,1)) for x in range(8)])
):
    # add the first item to the end of the list 
    # so we can look at it without fancy shit later
    seq.append(seq[-1])
    # go through them all except the last cuz it's a dummy
    new_sequence = []
    for i, element in enumerate(seq[:-1]):
        # make a tuple of the iterated and its neighbors
        neighbors = ((seq[i-1], seq[i], seq[i+1]))
        # look up the base sequence index to map to the rule
        base_index = base_sequence.index(neighbors)
        # get the rule result by index
        rule_result = rule[base_index]
        new_sequence.append(rule_result)
        # print(''.join(str(neighbors)), base_index, rule_result, '\n', new_sequence)
    print(''.join(new_sequence).replace('0', ' ').replace('1', '█'))
    sleep(0.025)
    graph([int(x) for x in new_sequence])

base_sequence = (
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1)
)

rule = { 
    '30':   '00011110',
    '54':   '00110110',
    '60':   '00111100',
    '62':   '00111110',
    '90':   '01011010',
    '94':   '01011110',
    '102':  '01100110',
    '110':  '01101110',
    '122':  '01111010',
    '126':  '01111110',
    '150':  '10010110',
    '158':  '10011110',
    '182':  '10110110',
    '188':  '10111100',
    '190':  '10111110',
    '220':  '11011100',
    '222':  '11011110',
    '250':  '11111010'
}

graph()
import os.path
from operator import itemgetter
from collections import OrderedDict

# Given   : file with inlink graph adjacency list representation
# example of txt file :
#
# Effect  : initializes the inlinks webgraph dictionary
''' initializes / populates  [Possible wrong use of word] '''

def load_inlink_webgraph(filename):
    inlink_dict = dict()
    values = []
    count = 1
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename) as f:
            line = f.readline()
            while line:
                key = line.split()[0]
                values = line.split()
                values.pop(0)
                inlink_dict[key] = values
                #print(key)
                #print(values)
                #print(line.split())
                #print("Line {}:    Key : {}     |     {}".format(count,key,line.strip()))
                line = f.readline()
                count += 1
    return inlink_dict

###############################################################################
''' Compute all outlinks of a page'''
# Given   :
# Returns :
def compute_outlinks(page,inlink_graph):
    outlinks = []  # list of outlinks (webpage docIDs)
    for key,value in inlink_graph.items():
        for pg in value:
            if pg == page:
                if key not in outlinks:
                    outlinks.append(key)
    return outlinks

###############################################################################

# Given   :
# Returns :

def compute_outlinks_graph(inlink_graph):
    outlink_dict = dict()
    for page in inlink_graph:
        outlinks = compute_outlinks(page,inlink_graph)
        outlink_dict[page] = outlinks
    return outlink_dict

###############################################################################

# Given   :
# Returns :

def find_sinks(outlink_graph):
    sink = []
    for page in outlink_graph:
        if(len(outlink_graph[page])==0):
            sink.append(page)
    return set(sink)

###############################################################################

# Given  :
# Effect :
def print_graph(webgraph):
    print('\n==========================================================================================================')
    for key, value in webgraph.items() :
        print("  {}".format(key).ljust(30),value)
    print('===========================================================================================================')

###############################################################################

# Given  :
# Effect :
def print_pageranks(PR):
    #sortedPR = sorted(PR.items(), key=operator.itemgetter(1), reverse=True)
    #sortedPR = sorted(PR.items(), key=lambda x: x[1])
    sortedPR = OrderedDict(sorted(PR.items(), key=itemgetter(1),reverse=True))
    print('\n==================================== Page Ranks==========================================================')
    for key, value in sortedPR.items() :
        print(" Page:  {}".format(key).ljust(50)," PageRank:  {}".format(value))
    print('===========================================================================================================')

###############################################################################

# Given   :
# Effect  :

def webgraph_Stats(webgraph):
    sink = [] # outlink count = 0
    source = [] # inlinks count is 0
    in_count = 0
    out_count = 0
    max_inlinks = 0
    max_outlinks = 0
    #avg_inlinks
    #avg_outlinks

    print("\n\t Web Graph Stats")
    print('\n\tNodes    : ',len(webgraph))
    for key, values in webgraph.items():
        outlnk = len(compute_outlinks(key,webgraph))
        out_count+=outlnk
        in_count+=len(values)
        if outlnk == 0:
            sink.append(key)
        if len(values) == 0:
            source.append(key)
        if(len(values) > max_inlinks):
            max_inlinks = len(values)
        if(outlnk > max_outlinks):
            max_outlinks = outlnk
    print('\tSinks    : ',len(sink))
    print('\t',sink)
    print('\tSources  : ',len(source))
    print('\t',source)
    print('\tMax number of inlinks for any node  : ',max_inlinks)
    print('\tMax number of outlinks for any node : ',max_outlinks)
    print('\tAverage inlinks per node            : ',(in_count/len(webgraph)))
    print('\tAverage outlinks per node           : ',(out_count/len(webgraph)))

###############################################################################

# Given   :
# Effect : Prints and writes to file

'''
def top50_pageranks():
    f=open("Top50PageRanks"+.txt",'w+')
    for page,value in G[0:50]
'''

###############################################################################

# -----------------------------------------------------------

# Given   :
# Effect  :
def write_graph_to_file():
    f= open('G2.txt','w')
    i=1
    for key,value in webgraph.items():
        f.write(('Webpage {} :'.format(i).ljust(15)))
        f.write(key)
        for inlink in value:
            f.write(" "+inlink)
        f.write("\n")
        i+=1
    f.close()
    print('\n\tKeys added to file : G2.txt')
    print('\n\t# of keys : {} '.format(i-1))
# ----------------------------------------------------------------------------

'''
if __name__ == "__main__":
    file_nm = "G2.txt"
    create_webgraph(file_nm)
    print_webgraph()
    print_all_outlinks(inlink_webgraph)
    #print_outlinks('D',inlink_webgraph)
    webgraph_Stats(inlink_webgraph)
'''
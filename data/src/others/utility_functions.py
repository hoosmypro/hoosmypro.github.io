# Neal Chen
# hc4pa  
import pydot

def generate_representation(master_list):
    graph = pydot.Dot(graph_type='graph')
    for i in range(9):
        for Class in master_list[i].list_of_Class:
            node1 = pydot.Node(master_list[i].id, style="filled", fillcolor="green")
            node2 = pydot.Node(Class.id + str(Class.number) + "\n" + Class.instructor.id, fillcolor="red")
            edge = pydot.Edge(node1, node2)
            graph.add_edge(edge)
            for Section in Class.list_of_Section:
                edge = pydot.Edge(Class.id + str(Class.number) + "\n" + Class.instructor.id, "N.O:" + str(Section.count) + "\n" + Section.comment + "\n"+ "Difficult:" + str(Section.difficult) + "\n" + "Difficult:" + str(Section.hotness))
                graph.add_edge(edge)
    graph.write_svg('example1_graph.svg')
    print("Graph generated")

def search_against_error():
    return 0

def format_generate():
    return 0


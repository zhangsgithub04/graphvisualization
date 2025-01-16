import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def create_graph():
    # Create a simple graph for demonstration
    G = nx.Graph()
    # Add nodes and edges
    G.add_node("Node 1", title="Node 1 details")
    G.add_node("Node 2", title="Node 2 details")
    G.add_node("Node 3", title="Node 3 details")
    G.add_edge("Node 1", "Node 2")
    G.add_edge("Node 2", "Node 3")
    G.add_edge("Node 3", "Node 1")
    return G

def draw_graph(graph, output_filename="graph.html"):
    # Create a Pyvis network
    net = Network(notebook=False, height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(graph)  # Convert NetworkX graph to Pyvis graph

    # Customize the physics of the network for better visualization
    net.show_buttons(filter_=['physics'])
    net.set_options("""
    var options = {
      "nodes": {
        "borderWidth": 2,
        "size": 30,
        "color": {
          "border": "#222222",
          "background": "#999999"
        },
        "font": {
          "color": "#ffffff"
        }
      }
    }
    """)
    
    # Save the graph visualization as an HTML file
    net.show(output_filename)

def display_graph(html_file):
    # Read the HTML file and display it in the Streamlit app
    with open(html_file, "r", encoding="utf-8") as f:
        html_data = f.read()
    components.html(html_data, height=750, scrolling=True)

# Main function to run the Streamlit app
def main():
    st.title("Interactive Graph Visualization")
    st.write("This is an interactive graph visualization using Pyvis and Streamlit.")

    # Create and display the graph
    graph = create_graph()
    draw_graph(graph)
    display_graph("graph.html")

# Run the app
if __name__ == "__main__":
    main()

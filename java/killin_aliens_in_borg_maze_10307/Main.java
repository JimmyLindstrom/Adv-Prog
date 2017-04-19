package killin_aliens_in_borg_maze_10307;

import java.io.*;
import java.util.*;

/**
 * Created by jimmy on 2016-10-06.
 */
class Main {
    InputStreamReader isr = null;
    BufferedReader br = null;
    Node startNode;

    final int[][] DIRECTIONS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};


    public int solve_maze() throws IOException {
        String[] widthAndHeight = br.readLine().split(" ");
        int width = Integer.parseInt(widthAndHeight[0]);
        int height = Integer.parseInt(widthAndHeight[1]);
        HashMap<Node, LinkedList<Edge>> graph = new HashMap<>();
        startNode = null;
        List<Edge> edges = new LinkedList<>();
        char[][] maze = new char[height][width];
        int[][] dist = new int[height][width];
        for (int x = 0; x < height; x++) {
            char[] row = br.readLine().toCharArray();
            for (int y = 0; y < width; y++) {
                try {
                    if (row[y] == 'S' || row[y] == 'A') {
                        Node node = new Node(x, y);
                        graph.put(node, new LinkedList<>());
                        if(row[y] == 'S')
                            startNode = node;
                    }
                    maze[x][y] = row[y];
                    dist[x][y] = 100;
                } catch (ArrayIndexOutOfBoundsException ai) {
                    maze[x][y] = '#';
                    dist[x][y] = 100;
                }
            }
        }
        // Run when startNode exists!
        if(startNode != null){
            // getting all the edges and their distances
            BFSSearch(graph, maze, startNode, edges, dist);
            graph.forEach((node, edge) -> {
                if (!node.equals(startNode)) {
                    resetDistances(dist);
                    BFSSearch(graph, maze, node, edges, dist);
                }
            });

            int distance = kruskal(edges);
            return distance; // ÄNDRA DETTA!!!
        }
        return 0;
    }

    //------------------- BFS SEARCH -----------------------------
    public void BFSSearch(HashMap<Node, LinkedList<Edge>> graph, char[][] maze, Node rootNode, List<Edge> edges, int[][] bfs){
        Queue<Node> node_queue = new LinkedList<>();
        node_queue.add(rootNode);
//        startNode.dist = 0;
        bfs[rootNode.x][rootNode.y] = 0;
        while(!node_queue.isEmpty()) {
            Node u = node_queue.remove();
            int x = u.x;
            int y = u.y;
            for(int[] dir: DIRECTIONS) {
                int newX = x + dir[0];
                int newY = y + dir[1];
                char nodeType = maze[newX][newY];
                if(nodeType != '#' && nodeType != 'S' && bfs[newX][newY] == 100) {
                    Node newNode = locate(new Node(newX, newY), graph);
//                        newNode.dist = bfs[x][y] + 1;
//                        System.out.println(newNode.print());
                    bfs[newX][newY] = bfs[x][y] + 1;
                    if(nodeType == 'A'){
                        Edge edge = new Edge(rootNode, newNode, bfs[newX][newY]);
                        if(!counterEdgeExists(edge, graph)) {
                            edges.add(edge);
                            graph.get(rootNode).add(edge);
                        }
                    } else if(nodeType == ' ') {
                        node_queue.add(newNode);
                    }
                }
            }
        }
    }

    // locate the Node in nodes array. If it doesn't
    // exist, send back the new Node
    private Node locate(Node u, HashMap<Node, LinkedList<Edge>> graph) {
        for(Map.Entry<Node, LinkedList<Edge>> entry: graph.entrySet()){
            if (entry.getKey().equals(u))
                return entry.getKey();
        }

        return u;
    }

    private boolean counterEdgeExists(Edge edge, HashMap<Node, LinkedList<Edge>> graph) {
        for(Edge e: graph.get(edge.to)){
            if (e.to.equals(edge.from) && e.from.equals(edge.to))
                return true;
        }
        return false;
    }

    // ------------------- BFS SEARCH END --------------------------

    private void resetDistances(int[][] bfs) {
        for(int i = 0; i < bfs.length; i++) {
            for(int j = 0; j < bfs[i].length; j++) {
                bfs[i][j] = 100;
            }
        }
    }

    // Calculating MST and returning the minimum distance!
    private int kruskal(List<Edge> edges) {
        int distance = 0;
        LinkedList<Edge> mst = new LinkedList<>();
        Collections.sort(edges, (e1, e2) -> Integer.compare(e1.weight, e2.weight));
        for (Edge e : edges) {
            if(!find(e.from).equals(find(e.to))){
                mst.add(e);
                union(e.from, e.to);
                distance += e.weight;
            }
        }
        return distance;
    }

    // ------- Union find Algorith ----------
    public void union(Node x, Node y) {
        Node x_root = find(x);

        Node y_root = find(y);

        if(x_root == y_root) {
            return;
        }
        if (x_root.rank < y_root.rank) {
            x_root.parent = y_root;
        }
        else if (x_root.rank > y_root.rank) {
            y_root.parent = x_root;
        } else {
            y_root.parent = x_root;
            x_root.rank = x_root.rank + 1;
        }
    }
    public Node find(Node x) {
        if (x.parent != x)
            x.parent = find(x.parent);
        return x.parent;
    }

    // --------- Union find end --------------



    public void run() throws IOException {
        isr = new InputStreamReader(System.in);
// -------------- FOR READING LOCAL FILE -------------
        String path = "killin_aliens_in_borg_maze_10307/input_data.txt";
        isr = new InputStreamReader(new FileInputStream(new File(path)));
// ---------------------------------------------------
        br = new BufferedReader(isr);
        int cases = Integer.parseInt(br.readLine());
        for (int i = 0; i < cases; i++) {
            System.out.println(solve_maze());
        }
    }

    public static void main(String[] args) {
        Main program = new Main();
        try {
            program.run();
        } catch (IOException io) {
            System.out.println("IOEXCEPTION");
        }
    }


}
// Supporting classes for Node and Edge
// -------------------------------------
class Node {
    int x, y, rank;
    Node parent;

    Node(int x, int y) {
        this.x = x;
        this.y = y;
        this.rank = 0;
        this.parent = this;
    }

    public String print() {
        return "(X: " + this.x + ", Y: " + this.y + " )";
    }

    @Override
    public boolean equals(Object obj) {
        if(obj instanceof Node) {
            Node temp = (Node)obj;
            if (this.x == temp.x && this.y == temp.y)
                return true;
        }
        return false;
    }

}

class Edge {
    Node to, from;
    int weight;

    Edge(Node from, Node to, int weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }

    public String print() {
        return this.from.print() + "---->" + this.to.print() + " = " + this.weight + " distance";
    }

}

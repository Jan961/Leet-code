public class Main {



    public void breadthFirstTraversal(){
        TreeNode current = this.root;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(current);
        while (!queue.isEmpty()){
          current = queue.poll();
          System.out.print(current.data + " ");
          queue.addAll(current.children);  
        }
    
      }


        public static void depthFirstTraversal(Vertex start, ArrayList<Vertex> visitedVertices) {
          System.out.println(start.getData());
      
          for (Edge e: start.getEdges()) {
            Vertex neighbor = e.getEnd();
      
            if (!visitedVertices.contains(neighbor)) {
              visitedVertices.add(neighbor);
              GraphTraverser.depthFirstTraversal(neighbor, visitedVertices);
            }
          }
        }
      
        public static void breadthFirstTraversal(Vertex start, ArrayList<Vertex> visitedVertices) {
          for(Edge e : start.getEdges()) {
            Vertex neighbor = e.getEnd();
            if(!visitedVertices.contains(neighbor)) {
              visitedVertices.add(neighbor);
            }
          }
        }
    
}

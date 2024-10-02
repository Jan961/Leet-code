public class Main {

    public void insert(int value){
        if (this.value > value){
          if (this.left == null){
            this.left = new BinarySearchTree(value);
          }
          else{
            this.left.insert(value);
          }
        }
        else{
          if (this.right == null){
            this.right = new BinarySearchTree(value);
          }
          else{
            this.right.insert(value);
          }
    
        }
    
      }
    
}

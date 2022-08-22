public class testing {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

        public TreeNode() {
        }
    }

    public void lowestCommonAncesetor(TreeNode root, TreeNode p, TreeNode q) {
        while(true){
            if(root.val < p.val && p.val < q.val)
                root = root.left;  
            else if(root.val > p.val && p.val > q.val)
                root = root.right;
            else
                break;
        }
    }

}

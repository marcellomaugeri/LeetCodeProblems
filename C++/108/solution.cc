/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = (left + right) / 2; 
        TreeNode* root = new TreeNode(nums[mid]);
        buildTree(root, left, mid - 1, nums);
        buildTree(root, mid + 1, right, nums);
        return root;
    }
private:
    void buildTree(TreeNode* parent, int left, int right, vector<int>& nums) {
        if (left > right) {
            return;
        }
        int mid = (left + right) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        if (node->val < parent->val) {
            parent->left = node;
        } else {
            parent->right = node;
        }
        buildTree(node, left, mid - 1, nums);
        buildTree(node, mid + 1, right, nums);
    }
};
/*错误示范
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>>res = new LinkedList<>();
        for(int i = 0;i<nums.length;i++)
        {
            int l = i+1;
            int r = nums.length-1;
            while(l<r){
                if(nums[l]+nums[r]==-nums[i]){
                //res.add(Listnums[i],nums[l],nums[r]);这样写会出错，应该把加进去的数当成list
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    
                }
                else if(nums[l]+nums[r]+nums[i]<0){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return res;
    }
}*/

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>>res = new LinkedList<>();
        for(int i = 0;i<nums.length-2;i++)
        {
            int l = i+1;
            int r = nums.length-1;
            if(i==0||(i>0&&nums[i]!=nums[i-1])){
                while(l<r){
                    if(nums[l]+nums[r]==-nums[i]){
                //res.add(Listnums[i],nums[l],nums[r]);这样写会出错，应该把加进去的数当成list
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                 //trick:跳过相同的结果
                    while(l<r&&nums[l]==nums[l+1])
                        l++;
                    while(l<r&&nums[r]==nums[r-1])
                        r--;
                    l++;
                    r--;
                }
                else if(nums[l]+nums[r]<-nums[i]){
                    l++;
                }else{
                    r--;
                }
            }
            
            }
        }
        return res;
    }
}

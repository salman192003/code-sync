function subsets(nums: number[]): number[][] {
    
    let result : number[][] = [];
    
    function helper(index:number, path : number[] )
    {
        if(index == nums.length)
        {
            result.push([...path]);
            return;
        }

        //include the subset
        path.push(nums[index]);
        helper(index+1,path);
        path.pop();

        helper(index + 1,path);
        
    }

    helper(0,[]);
    
    return result;
};
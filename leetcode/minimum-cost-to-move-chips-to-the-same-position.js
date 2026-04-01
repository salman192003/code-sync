function minCostToMoveChips(position: number[]): number {
     let evengroup = 0;
    let oddgroup = 0;
    for (const pos of position)
    {
        if (pos % 2 == 0)
        {
            evengroup = evengroup + 1;
        }
        else
        {
            oddgroup = oddgroup + 1;
        }
    }

    //now that I know which group most belong in
    // if most in the even, calculate the cost needed to convert them into even

    if ( oddgroup < evengroup)
    {
        return oddgroup;
    }
    else {
        return evengroup
    }

};
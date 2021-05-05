// int longest = 0;
        // int max = arr[0];
        // int k = 0;                
        // if(arr.length< 3){              //checks to see if array can be a mountain or not
        //     return longest;
        // }
        // for (int a = 0; a < arr.length; a++){                   // For loop to find the largest number in array to use as pivot
        //     if( arr [a] > max){
        //         max = arr[a];
        //         k = a;
        //     }
        // }
        // if( k == arr.length-1 || k == 0){
        //     return 0;
        // }
        // for( int index = k ; index >= 0 ; index --){
        //     if(index == 0){
        //         if(arr[index] < arr[index + 1]){
        //             System.out.println(arr[index]);
        //             longest++;
        //             break;
        //         }
        //     }
        //     if (arr[index-1] < arr[index]){
        //         System.out.println(arr[index]);
        //         longest++;
        //     }
        //     else{
        //         System.out.println(arr[index]);
        //         longest++;
        //         break;
        //     }
        // }
        // for( int index = k+1  ; index <= arr.length-1 ; index++){
        //     if(index == arr.length-1){
        //         if(arr[index] < arr[index-1]){
        //             System.out.println(arr[index]);
        //             longest++;
        //             break;
        //         }else {
        //             longest = 0;
        //             break;
        //         }
        //     }
        //     if ( arr[index+1] < arr[index]){
        //         System.out.println(arr[index]);
        //         longest++; 
        //     }
        //     else{
        //         System.out.println(arr[index]);
        //         longest++;
        //         break;
        //     }
        // }  
        // return longest;
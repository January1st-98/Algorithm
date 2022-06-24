//
//  15652.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/22.
//

var inputs = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var array: [Int] = Array(repeating: 0, count: 10)
var ans: String = ""
func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans += "\(array[i]) "
        }
        ans += "\n"
        return
    }
    
    for i in 1...n {
        if count == 0 {
            array[count] = i
            solve(count+1)
        } else {
            if(array[count-1] > i) { continue }
            array[count] = i
            solve(count+1)
        }
    }
}
solve(0)
print(ans)


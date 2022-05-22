//
//  15651.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/22.
//

var inputs = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var array: [Int] = Array(repeating: 0, count: 10)
var ans = ""
func solve(_  count: Int) -> Void {
//    print("solve(\(count))")
    if count == m {
        for i in 0..<m {
            ans += "\(array[i]) "
        }
        ans += "\n"
        return
    }
    
    for i in 1...n {
        array[count] = i
        solve(count+1)
    }
}
solve(0)
print(ans)

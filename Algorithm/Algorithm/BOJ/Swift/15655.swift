//
//  15655.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/22.
//

var inputs: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var array = Array(repeating: 0, count: 10)
var vis: [Bool] = Array(repeating: false, count: 10)

var numbers = readLine()!.split(separator: " ").map{ Int(String($0))! }
numbers = numbers.sorted(by: <)

var ans = ""

func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans += "\(array[i]) "
        }
        ans += "\n"
        return
    }
    
    for i in 0..<n {
        if vis[i] { continue }
        if count == 0 || (count != 0 && array[count-1] < numbers[i]) {
            vis[i] = true
            array[count] = numbers[i]
            solve(count+1)
            vis[i] = false
        }
    }
}
solve(0)
print(ans)

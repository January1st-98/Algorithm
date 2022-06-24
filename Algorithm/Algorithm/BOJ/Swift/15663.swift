//
//  15663.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/23.
//

// 중복되는 수열을 여러번 출력해서는 안된다.
var inputs = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var numbers = readLine()!.split(separator: " ").map{ Int(String($0))! }
var array = Array(repeating: 0, count: 10)
var isused = Array(repeating: false, count: 10)
var ans = ""

numbers = numbers.sorted(by: <)
func solve(_ count: Int) -> Void {
    if count == m {
        for i in 0..<m {
            ans.write(String(array[i]) + " ")
        }
        ans.write("\n")
        return
    }
    var tmp: Int = 0
    for i in 0..<n {
        if isused[i] || tmp == numbers[i] { continue }
        isused[i] = true
        array[count] = numbers[i]
        tmp = numbers[i]
        solve(count+1)
        isused[i] = false
    }
    
}
solve(0)
print(ans)


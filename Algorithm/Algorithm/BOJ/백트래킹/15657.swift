//
//  15657.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/23.
//

var inputs: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var numbers: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
var array: [Int] = Array(repeating: 0, count: 10)
var ans: String = ""
numbers = numbers.sorted(by: <)

// count개의 숫자를 고름
func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans.write(String(array[i]) + " ")
        }
        ans.write("\n")
        return
    }
    
    for i in 0..<n {
        if count == 0 {
            array[count] = numbers[i]
            solve(count+1)
        } else {
            if array[count-1] > numbers[i] { continue }
            array[count] = numbers[i]
            solve(count+1)
        }
    }
}
solve(0)
print(ans)



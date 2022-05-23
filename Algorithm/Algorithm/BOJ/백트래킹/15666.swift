//
//  15666.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/24.
//

///https://www.acmicpc.net/problem/15666
///같은 수를 여러번 골라도 되는 수열
///수열이 오름차순 이어야함.

var inputs = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var array = Array(repeating: 0, count: 10)
var numbers = readLine()!.split(separator: " ").map{ Int(String($0))! }
var ans = ""

numbers = numbers.sorted(by: <)

func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans.write(String(array[i]) + " ")
        }
        ans.write("\n")
        return
    }
    var tmp = -1
    for i in 0..<n {
        if tmp == numbers[i] { continue }
        if count == 0 {
            array[count] = numbers[i]
            tmp = numbers[i]
            solve(count + 1)
        } else {
            if array[count-1] > numbers[i] { continue }
            array[count] = numbers[i]
            tmp = numbers[i]
            solve(count + 1)
            
        }
    }
}
solve(0)
print(ans)


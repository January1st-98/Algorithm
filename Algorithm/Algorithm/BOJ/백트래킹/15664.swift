//
//  15664.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/23.
//


///https://www.acmicpc.net/problem/15664
///중복되는 수열을 여러번 출력해서는 안된다.
///수열은 사전순으로 증가하는 순서로 출력한다.
///수열이 비 내림차순이여야한다.

var inputs = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var numbers = readLine()!.split(separator: " ").map{ Int(String($0))! }
numbers = numbers.sorted(by: <)
var array = Array(repeating: 0, count: 10)
var isused = Array(repeating: false, count: 10)

var ans = ""

func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans.write(String(array[i]) + " ")
        }
        ans.write(String("\n"))
        return
    }
    var tmp = -1
    for i in 0..<n {
        if isused[i] || tmp == numbers[i] { continue }
        // 아직 아무런 수도 구하지 않았을 때.
        if count == 0 {
            isused[i] = true
            array[count] = numbers[i]
            tmp = numbers[i]
            solve(count+1)
            isused[i] = false
        } else {
            if numbers[i] < array[count-1] { continue }
            isused[i] = true
            array[count] = numbers[i]
            tmp = numbers[i]
            solve(count+1)
            isused[i] = false
        }
    }
    
}
solve(0)
print(ans)

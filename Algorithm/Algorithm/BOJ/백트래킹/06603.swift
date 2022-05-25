//
//  06603.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/24.
//

var input: [Int] = []
var sum = 1
var visited = Array(repeating: false, count: 13)
var result: [Int] = []

while true {
    // input이 애초에 오름차순으로 주어지기 때문에 정렬할 필요가 없다.
    input = readLine()!.split(separator: " ").map{ Int(String($0))! }
    if input[0] == 0 { break }
    input.removeFirst()
    solve(0, 0)
    print("")
}

func solve(_ count: Int, _ start: Int) {
    if count == 6 {
        print(result.map{String($0)}.joined(separator: " "))
        return
    }
    for i in start..<input.count {
        if !visited[i] {
            visited[i] = true
            result.append(input[i])
            solve(count+1, i)
            result.removeLast()
            visited[i] = false
        }
    }
}

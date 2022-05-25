//
//  01759.swift
//  Algorithm
//
//  Created by Jaehoon So on 2022/05/24.
//

///암호는 서로다른 L개의 알파벳 소문자들로 구성된다.
///최소 한개의 모음(a, e, i, o, u)와 최소 두개의 자음으로 구성되어 있다.
///암호를 이루는 알파벳은 암호에서 증가하는 순서로 배열되어있다.

var input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let L = input[0], C = input[1]

var alphabets: [String] = readLine()!.split(separator: " ").map{ String($0) }
alphabets.sort(by: <) // 알파벳을 정렬한다.
var array: [String] = []
var str: String = ""
var isused: [Bool] = Array(repeating: false, count: 15)
// count: 뽑은 알파벳의 수
// start: 직전 알파벳의 alphabets 배열에서의 인덱스
func solve(_ count: Int, _ start: Int) {
    if count == L {
        var vowel: Int = 0
        var consonent: Int = 0
        for i in 0..<L {
            var ch: String = array[i]
            if ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u" { vowel += 1 }
            else { consonent += 1 }
        }
        if vowel < 1 || consonent < 2 { return }
        for i in 0..<L {
            str += array[i]
        }
        str += "\n"
    }
    for i in start..<C {
        if isused[i] { continue }
        array.append(alphabets[i])
        isused[i] = true
        solve(count+1, i)
        isused[i] = false
        array.removeLast()
    }
    
}
solve(0, 0)
print(str)


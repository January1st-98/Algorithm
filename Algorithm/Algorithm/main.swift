var inputs: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = inputs[0], m = inputs[1]
var array = Array(repeating: 0, count: 10)

var numbers = readLine()!.split(separator: " ").map{ Int(String($0))! }
numbers = numbers.sorted(by: <)

var ans = ""

func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            ans.write(String(array[i]) + " ")
        }
        ans.write("\n")
        return
    }
    
    for i in 0..<n {
        array[count] = numbers[i]
        solve(count+1)

    }
}
solve(0)
print(ans)

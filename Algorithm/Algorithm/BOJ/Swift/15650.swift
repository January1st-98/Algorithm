var inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let n = inputs[0], m = inputs[1]
var vis: [Bool] = Array(repeating: false, count: 10)
var ans: [Int] = Array(repeating: 0, count: 10)
func solve(_ count: Int) {
    if count == m {
        for i in 0..<m {
            print(ans[i], terminator: " ")
        }
        print("")
        return
    }
    
    for i in 1...n {
        if !vis[i] && count == 0 {
            vis[i] = true
            ans[count] = i
            solve(count + 1)
            vis[i] = false
        }
        if !vis[i] && count != 0 {
            if ans[count-1] > i { continue }
            vis[i] = true
            ans[count] = i
            solve(count + 1)
            vis[i] = false
        }
    }
}
solve(0)

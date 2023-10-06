from time import now

fn Sum(max: Int) -> Int64:
    var result:Int64 = 0
    for i in range(3, max):
        if i%3==0 or i%5==0: 
            result = result + i
    return result

fn SumDivisibleBy(n: Int64, max: Int64) -> Int64:
    let d = max / n
    return n * (d * (d+1))/2

fn main():
    let max = 1000
    var tic = now()
    print(Sum(max))
    print((now()-tic)/1e6, "ms")

    tic = now()
    print(SumDivisibleBy(3, max) + SumDivisibleBy(5, max) - SumDivisibleBy(15, max))
    print((now()-tic)/1e6, "ms")

    
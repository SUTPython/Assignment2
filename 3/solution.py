def parse_numbers(line):
    line = line.strip()
    if ',' in line:
        return [int(x.strip()) for x in line.split(',')]
    return list(map(int, line.split()))

def find_valid_pairs(powers, allowed_diffs, target_sum, min_distance):
    result = []
    n = len(powers)
    
    # Try all possible pairs
    for i in range(n):
        for j in range(i + min_distance, n):
            a, b = powers[i], powers[j]
            diff = abs(a - b)
            
            
            if diff not in allowed_diffs:
                continue
          
            if target_sum is not None and target_sum != "None":
                if a + b != target_sum:
                    continue
            
            
            pair = sorted([a, b])
            if pair not in result:
                result.append(pair)
    
    # Sort the result list for consistent output
    return sorted(result)

def main():
        import sys
        
        line1 = sys.stdin.readline().strip()
        if line1.isdigit():
         
            n = int(line1)
            powers = parse_numbers(sys.stdin.readline())
        else:
          
            powers = parse_numbers(line1)
        
      
        line = sys.stdin.readline().strip()
        if line.isdigit():
            
            m = int(line)
            allowed_diffs = parse_numbers(sys.stdin.readline())
        else:
        
            allowed_diffs = parse_numbers(line)
        
        target_sum_line = sys.stdin.readline().strip()
        target_sum = None if target_sum_line == 'None' else target_sum_line
        if target_sum is not None and target_sum != "None":
            target_sum = int(target_sum)
        
        min_distance = int(sys.stdin.readline())
        
        result = find_valid_pairs(powers, allowed_diffs, target_sum, min_distance)
        
        print(result)
        
        


if __name__ == "__main__":
    main() 
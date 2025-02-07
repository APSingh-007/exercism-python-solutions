def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    largest = 0
    factors = []

    for a in range(max_factor, min_factor - 1, -1):
        """
        Loop over all the possible factors:
            a goes from max --> min
            b goes from max --> a
        This gives the combination of all factors (a,b) possible with same factor can repeat twice;
        So, [1,1] and [2,2] is valid, but [2,1] is same as [2,1]
        """
        larger_product_found = False  # This stays false if there is no value of b for the current value of a for which a*b > largest palindrome
        for b in range(max_factor, a - 1, -1):
            product = a * b

            if product >= largest:
                """ 
                If for some value of b, a*b >= largest (which is 0 at start),
                then we can check it for palindrome
                
                larger_product_found:   set to 'True' if a product larger than the current largest palindrome
                                        is found in the current run of values of 'b' for same 'a'
                If larger_product_found remains false throughout this loop, that means NO further value of
                a*b will be larger than current largest palindrome, and we can break both the inner and outer loop
                """
                larger_product_found = True
                num_string = str(product)

                if num_string == num_string[::-1]:
                    if product > largest:
                        # If the new palindrome is larger, then factors need to be reset else,
                        # If product is same as previous, then can just be appended (outside if)
                        factors = []
                    largest = product
                    factors.append([a, b])
            else:
                """
                This excecutes when a product < largest, meaning for any further value of 'b' 
                with current value of 'a' will give a*b less than current value of the same.
                So, break out of inner loop to reduce unnecessary calculations
                """
                break

        if not larger_product_found:
            # Excecutes, if the current value of 'a' did not yeild a larger product, so the next value of 'a',
            # which will be even smaller than current value, cannot provide larger palindrome, so,
            # break out of loop to save unnecessary calculations
            break
    return (largest, factors) if largest else (None, [])


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    smallest = 0
    factors = []

    for a in range(min_factor, max_factor + 1):
        smaller_product_found = False
        for b in range(a, max_factor + 1):
            product = a * b

            if product <= smallest or smallest == 0:
                """ 
                If for some value of b, a*b <= smallest (or if smallest = 0),
                then we can check it for smallest palindrome
                
                smaller_product_found:  Set to 'True', if product smaller than the current smallest palindrome
                                        is found in the current run of values of 'b' for same 'a'
                If smaller_product_found remains false throughout this loop, that means NO further value of
                a*b will be smaller than current smallest palindrome, and we can break both the inner and outer loop
                """

                smaller_product_found = True
                num_string = str(product)

                if num_string == num_string[::-1]:
                    if product < smallest:
                        # If the new palindrome is larger, then factors need to be reset else,
                        # If product is same as previous, then can just be appended (outside if)
                        factors = []
                    smallest = product
                    factors.append([a, b])
            else:
                """
                This excecutes when a product > smallest, meaning for any further value of 'b' 
                with current value of 'a' will give a*b greater than current value of the same.
                So, break out of inner loop to reduce unnecessary calculations
                """
                break

        if not smaller_product_found:
            # Excecutes, if the current value of 'a' did not yeild a smaller product, so the next value of 'a',
            # which will be larger than current value, will never provide smaller palindrome, so,
            # break out of loop to save unnecessary calculations
            break

    return (smallest, factors) if smallest else (None, [])

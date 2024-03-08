def pascal_triangle(n):
        # Initialize the Pascal's triangle list
            triangle = []

                # Base case: return an empty list if n is less than or equal to 0
                    if n <= 0:
                                return triangle

                                # Iterate through each row of the triangle
                                    for i in range(n):
                                                # Initialize a new row list
                                                        row = []

                                                                # Calculate values for the current row
                                                                        for j in range(i + 1):
                                                                                        # If it's the first or last element of the row, append 1
                                                                                                    if j == 0 or j == i:
                                                                                                                        row.append(1)
                                                                                                                                    # Otherwise, calculate the value based on the previous row
                                                                                                                                                else:
                                                                                                                                                                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

                                                                                                                                                                            # Append the row to the triangle list
                                                                                                                                                                                    triangle.append(row)

                                                                                                                                                                                        return triangle


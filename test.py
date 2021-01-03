from parse_images import parse

colors = ['g', 'y', 'b', 'r']
total_columns = 10
total_rows = 6
grid_rows = 10
grid_columns = 4

files = ['06.jpg']
hour = 6

book = parse(files, hour, colors, total_columns, total_rows, grid_rows, grid_columns)

book.save("output.xlsx")

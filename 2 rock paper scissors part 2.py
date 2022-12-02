# get data from local txt file
with open('data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

# variable for storing total score
total_score = 0
# remember which letter represents win draw and loss. could remember "A"=rock and so on too, but isn't really needed
loss, draw, win = "X", "Y", "Z"
# remember how many points each outcome is worth
loss_points, draw_points, win_points = 0, 3, 6
rock_points, paper_points, scissors_points = 1, 2, 3

# iterate through the moves in the data
for move in data:
    match move[0]:
        # if opponent played rock
        case "A":
            # and we should win
            if move[2] in win:
                # play paper, calculate points for paper + points for winning
                total_score += paper_points + win_points
            # and we should draw
            elif move[2] in draw:
                total_score += rock_points + draw_points
            # and we should lose
            elif move[2] in loss:
                total_score += scissors_points + loss_points
        # if opponent played paper
        case "B":
            # and we should win
            if move[2] in win:
                total_score += scissors_points + win_points
            # and we should draw
            elif move[2] in draw:
                total_score += paper_points + draw_points
            # and we should lose
            elif move[2] in loss:
                total_score += rock_points + loss_points
        # if opponent played scissors
        case "C":
            # and we should win
            if move[2] in win:
                total_score += rock_points + win_points
            # and we should draw
            elif move[2] in draw:
                total_score += scissors_points + draw_points
            # and we should lose
            elif move[2] in loss:
                total_score += paper_points + loss_points

# print out the answer
print(f"Answer is: {total_score}")


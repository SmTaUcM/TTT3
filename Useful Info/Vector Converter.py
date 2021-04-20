xOffset = 0.4 # netative moves right, positive moves left.
yOffset = -5.0 # negative moves up, positive moves down.
zOffset = 0.0 # negative moves towards chest, positive moves away from chest.

boundMin = "<73.352531, -133.862488, 197.740814>"
boundMax = "<96.213715, -125.819641, 203.273270>"
vertex_vectors = """
        <73.949310, -131.677689, 198.161392>,
		<95.359924, -126.619453, 198.161392>,
		<95.171432, -125.821609, 202.484329>,
		<73.760818, -130.879837, 202.484344>,
		<73.789398, -131.833115, 197.988327>,
		<95.572479, -126.686890, 197.988327>,
		<95.367592, -125.819641, 202.687302>,
		<73.584518, -130.965866, 202.687302>,
		<73.667641, -132.069458, 197.850723>,
		<95.787132, -126.843750, 197.850723>,
		<95.567436, -125.913826, 202.889313>,
		<73.447945, -131.139526, 202.889313>,
		<73.597069, -132.361389, 197.763306>,
		<95.980888, -127.073242, 197.763306>,
		<95.749557, -126.094070, 203.068741>,
		<73.365738, -131.382217, 203.068741>,
		<73.590736, -132.683609, 197.740814>,
		<96.130753, -127.358559, 197.740814>,
		<95.892548, -126.350281, 203.203934>,
		<73.352531, -131.675323, 203.203934>,
		<73.661682, -133.010773, 197.798004>,
		<96.213715, -127.682877, 197.798004>,
		<95.974983, -126.672363, 203.273254>,
		<73.422951, -132.000259, 203.273270>,
		<73.822960, -133.317566, 197.949615>,
		<96.206787, -128.029419, 197.949615>,
		<95.975449, -127.050232, 203.255066>,
		<73.591629, -132.338379, 203.255066>,
		<74.087616, -133.578659, 198.210403>,
		<96.086960, -128.381348, 198.210403>,
		<95.872551, -127.473801, 203.127701>,
		<73.873207, -132.671127, 203.127701>,
		<74.468689, -133.768738, 198.595093>,
		<95.831238, -128.721863, 198.595093>,
		<95.644867, -127.932968, 202.869522>,
		<74.282310, -132.979843, 202.869522>,
		<74.979225, -133.862488, 199.118439>,
		<95.416626, -129.034164, 199.118423>,
		<95.270981, -128.417648, 202.458893>,
		<74.833572, -133.245956, 202.458893>
"""

def translateVectors(input):
    out = ""
    counter = 1

    for item in input.replace("<", "").replace(">", "").split(","):

        # X Translation - Left/Right.
        if counter == 1:
            out += "\t\t<" + str(float(item.replace("\n", "").replace("\t", "")) - xOffset) + ", "
            counter += 1

        # Z Translation - In/Out.
        elif counter == 2:
            out += str(float(item) - zOffset) + ", "
            counter += 1

        # Y Translation - Up/Down.
        elif counter == 3:
            out += str(float(item) - yOffset) + ">,\n"
            counter = 1

    print(str(out[:-2]))


translateVectors(boundMin)
print("\n")
translateVectors(boundMax)
print("\n")
translateVectors(vertex_vectors)

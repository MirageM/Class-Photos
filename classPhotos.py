#Class Photos
#Time Complexity: O(nlog(n)) || Space Complexity: O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    shirtColorInFirstRow = "red" if redShirtHeights[0] < blueShirtHeights[0] else "blue"
    for i in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[i]
        blueShirtHeight = blueShirtHeights[i]
        if shirtColorInFirstRow == "red":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True
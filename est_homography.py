import numpy as np
def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####
    A = []

    for i in range(X.shape[0]):
        a_x = np.array([-X[i][0], -X[i][1], -1, 0, 0, 0, np.multiply(X[i][0], X_prime[i][0]), np.multiply(X[i][1], X_prime[i][0]), X_prime[i][0]])
        a_y = np.array([0, 0, 0, -X[i][0], -X[i][1], -1, np.multiply(X[i][0], X_prime[i][1]), np.multiply(X[i][1], X_prime[i][1]), X_prime[i][1]])
        A.append(a_x)
        A.append(a_y)

    [U, S, Vt] = np.linalg.svd(np.array(A))
    V = np.transpose(Vt)
    H = V[:, -1].reshape(3,3)
    #print(H)

    ##### STUDENT CODE END #####

    return H

import pickle

from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree

instances = [[0], [1], [2], [3]]
classification = [0, 0, 1, 1]

voting_predictions = []
hybrid_stacking_predictions = []

def main():
    evaluation_set = [[5], [43], [8], [0], [1]]

    voting(evaluation_set)
    #hybrid_stacking(evaluation_set)

    for e in voting_predictions:
        print(e)

def voting(evaluation_set):
    print('[voting] Treinando os modelos...')
    # KNN
    classifier_knn = KNeighborsClassifier(n_neighbors=3)
    classifier_knn.fit(instances, classification)

    # SVM
    classifier_svm = svm.SVC(kernel='linear', C = 1.0)
    classifier_svm.fit(instances, classification)

    # Decision Trees
    classifier_dt = tree.DecisionTreeClassifier()
    classifier_dt.fit(instances, classification)

    print('[voting] Utilizando os modelos para novas predicoes...')
    for instance in evaluation_set:
        #classifier_knn.predict([[1.1]])
        prediction_knn = classifier_knn.predict([instance])
        prediction_svm = classifier_svm.predict([instance])
        prediction_dt = classifier_dt.predict([instance])

        predictions_sum = prediction_knn + prediction_svm + prediction_dt

        # Votacao majoritaria
        final_prediction = 0
        if predictions_sum > 1:
             final_prediction = 1

        voting_predictions.append(final_prediction)


def hybrid_stacking(evaluation_set):
    print('[hybrid_stacking] Treinando os modelos...')


    print('[hybrid_stacking] Utilizando os modelos para novas predicoes...')
    for instance in evaluation_set:
        #pred = vote_and_classify(instance)
        hybrid_stacking_predictions.append(pred)



if __name__ == '__main__':
    main()

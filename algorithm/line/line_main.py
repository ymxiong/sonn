import dataset.simple.simple_dataset_generator as generator
import algorithm.line.structure.cell as cell
import algorithm.line.structure.observer as observer

training_set = generator.generate_train_set()
test_set = generator.generate_test_set()


observer = observer.Observer()
feature_cell_set = [cell.FeatureCell("F1", observer), cell.FeatureCell("F2", observer)]
target_cell_set = [cell.TargetCell("TA", observer), cell.TargetCell("TB", observer)]


# 逐项训练
for item in training_set:
    observer.init()

    if item[2] == "A":
        target_cell_set[0].activation(1)
    elif item[2] == "B":
        target_cell_set[1].activation(1)

    feature_cell_set[0].accumulation(item[0])
    feature_cell_set[1].accumulation(item[1])

    feature_cell_set[0].activation()
    feature_cell_set[1].activation()

    observer.run()

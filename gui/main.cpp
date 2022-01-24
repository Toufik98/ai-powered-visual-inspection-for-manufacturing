#include <QApplication>
#include <QQmlApplicationEngine>


#include <QQmlEngine>
#include <QQmlContext>



int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    //QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QQmlApplicationEngine engine;

    engine.load(QUrl(QStringLiteral("main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;


    return a.exec();
}

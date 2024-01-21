using System;
using System.Threading;
using UnityEngine;

public class GeneticAlgorithm : MonoBehaviour
{
    public GameObject Dot;

    public int size;
    public int mutation;
    public int generations;

    int[] integers;  
    String[] binarys;
    Double[] fitness;
    String[] children;

    int aux01 = 0;
    int aux02 = 0;

    //Cria um array de numeros inteiros aleatórios (de 0 a 1024), cuja quantidade de elementos é definida pela variável size.
    //Converte os elementos do array de inteiros para binários e armazena no array binarys.
    void Start()
    {
        integers = new int[size];
        binarys = new String[size];
        fitness = new double[size];
        children = new String[size];

        for (int i = 0; i < integers.Length; i++)
        {
            integers[i] = new System.Random().Next(1024);
            Thread.Sleep(15);
        }
        binarys = decimalToBinary(integers);
        fitness = calculateFitness(integers);
    }

    //Instancia os pontos (filhos) no gráfico de acordo com o fitness.
    void Update()
    {
        if (aux01 < generations && aux02 < size)
        {
            GameObject dotInstance = Instantiate(Dot, new Vector3(integers[aux02], (float)fitness[aux02], 0), Quaternion.identity) as GameObject;
            Renderer rend = dotInstance.GetComponent<Renderer>();

            aux02++;
            //Destroy(dotInstance, 1);
            Thread.Sleep(50);
        }
        else if (aux01 < generations && aux02 >= size)
        {
            children = generateChild(binarys, fitness, mutation);
            binarys = children;
            integers = binariyToDecimal(binarys);
            fitness = calculateFitness(integers);

            aux02 = 0;
            aux01++;
        }
    }

    //Função que converte de binário para decimal.
    static int[] binariyToDecimal(String[] binarys)
    {
        int[] decimals = new int[binarys.Length];
        for (int i = 0; i < binarys.Length; i++)
        {
            decimals[i] = Convert.ToInt32(binarys[i], 2);
        }
        return decimals;
    }

    //Função que converte de decimal para binário.
    static String[] decimalToBinary(int[] integers)
    {
        String[] binarys = new String[integers.Length];

        for (int i = 0; i < binarys.Length; i++)
        {
            binarys[i] = Convert.ToString(integers[i], 2).PadLeft(11, '0');
        }
        return binarys;
    }

    //Função que calcula o fitness.
    static Double[] calculateFitness(int[] integers)
    {
        Double[] fitness = new Double[integers.Length];

        for (int i = 0; i < integers.Length; i++)
        {
            fitness[i] = 421 - Math.Abs(integers[i] * Math.Sin(Math.Sqrt(Math.Abs(integers[i]))));
        }
        return fitness;
    }

    //Função que realiza a reprodução.
    String[] generateChild(String[] binarys, Double[] fitness, int mutation)
    {
        String[] children = new String[binarys.Length];

        for (int i = 0; i < children.Length; i++)
        {
            int divider = new System.Random().Next(1, 10);
            
            int random01 = new System.Random().Next(0, binarys.Length);
            Thread.Sleep(15);
            int random02 = new System.Random().Next(0, binarys.Length);
            Thread.Sleep(15);

            String parent01 = (fitness[random01] < fitness[random02] ? binarys[random01] : binarys[random02]);
            
            random01 = new System.Random().Next(0, binarys.Length);
            Thread.Sleep(15);
            random02 = new System.Random().Next(0, binarys.Length);
            Thread.Sleep(15);
            
            String parent02 = (fitness[random01] < fitness[random02] ? binarys[random01] : binarys[random02]);
           
            String child = string.Concat(parent01.Substring(0, divider), parent02.Substring(divider));

            if (new System.Random().Next(1, 100) <= mutation)
            {
                int position = new System.Random().Next(0, 10);
                char[] childArray = child.ToCharArray();

                if(child[position] == '0')
                {
                    childArray[position] = '1';
                }

                else if(child[position] == '1')
                {
                    childArray[position] = '0';
                }
                child = new string(childArray);
            }
            children[i] = child;
        }
        return children;
    }
}
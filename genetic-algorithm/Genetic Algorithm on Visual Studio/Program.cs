using System;
using System.Threading;

namespace Lista_05___TAP
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Insira o tamanho da população (em número de indivíduos):");
            int popsize = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Defina a taxa de mutação (em porcentagem):");
            int muttax = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Defina quantas gerações serão produzidas:");
            int genamount = Convert.ToInt32(Console.ReadLine());
            int[] decimalarray = new int[popsize];
            string[] binaryarray = new string[popsize];
            double[] fitnessarray = new double[popsize];
            string[] sonarray = new string[popsize];
            
            Random rnd = new Random();

            Console.WriteLine("\n------------------------------PRIMEIRA GERAÇÃO------------------------------\n");

            for (int ct = 0; ct < popsize; ct++)
            {
                decimalarray[ct] = rnd.Next(1024);
                binaryarray[ct] = Convert.ToString(decimalarray[ct], 2).PadLeft(11, '0');
                fitnessarray[ct] = 421 - Math.Abs(decimalarray[ct] * Math.Sin(Math.Sqrt(Math.Abs(decimalarray[ct]))));

                Console.WriteLine((ct + 1) + " - Decimal: " + decimalarray[ct] + "    Binário: " + binaryarray[ct] + "    Fitness: " + fitnessarray[ct] + "\n");
            }

            char[] dad = new char[11];
            char[] mom = new char[11];
            char[] son = new char[11];

            for (int ctgen = 0; ctgen < genamount; ctgen++)
            {
                for (int ctpop = 0; ctpop < popsize; ctpop++)
                {
                    int psbdad1 = rnd.Next(popsize);
                    int psbdad2 = rnd.Next(popsize);
                    int psbmom1 = rnd.Next(popsize);
                    int psbmom2 = rnd.Next(popsize);
                    int cut = rnd.Next(11); //Ponto de recorte dos pais.
                    int mutroll = rnd.Next(100);

                    //Compara o fitness dos elementos sorteados e escolhe o menor.
                    dad = fitnessarray[psbdad1] < fitnessarray[psbdad2] ? binaryarray[psbdad1].ToCharArray() : binaryarray[psbdad2].ToCharArray();
                    mom = fitnessarray[psbmom1] < fitnessarray[psbmom2] ? binaryarray[psbmom1].ToCharArray() : binaryarray[psbmom2].ToCharArray();

                    //A cada loop o elemento da respectiva posição do array pai é adicionado à mesma posição do array filho, parando no ponto de recorte.
                    for (int ctdad = 0; ctdad <= cut; ctdad++)
                    {              
                        son[ctdad] = dad[ctdad];
                    }

                    //Funciona como o laço anterior, porém se inicia na posição de recorte e termina na posição 10.
                    for (int ctmom = cut; ctmom < 11; ctmom++)
                    {
                        son[ctmom] = mom[ctmom];
                    }

                    //Caso haja mutação, seleciona um gene aleatório e inverte seu valor binário.
                    if (mutroll < muttax)
                    {
                        int mutgene = rnd.Next(11);
                        son[mutgene] = son[mutgene] == '1' ? son[mutgene] = '0' : son[mutgene] = '1';
                    }

                    sonarray[ctpop] = new string(son);
                }

                binaryarray = sonarray;
                
                for (int ct = 0; ct < popsize; ct++)
                {
                    decimalarray[ct] = Convert.ToInt32(binaryarray[ct], 2);
                    fitnessarray[ct] = 421 - Math.Abs(decimalarray[ct] * Math.Sin(Math.Sqrt(Math.Abs(decimalarray[ct]))));
                }
            }

            Console.WriteLine("\n------------------------------ÚLTIMA GERAÇÃO------------------------------\n");

            for(int ct = 0; ct < popsize; ct++)
            {
                Console.WriteLine((ct + 1) + " - Decimal: " + decimalarray[ct] + "    Binário: " + binaryarray[ct] + "    Fitness: " + fitnessarray[ct] + "\n");
            }
        }
    }
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejemploamano;

import javax.swing.JLabel;
import javax.swing.JTextField;

public class EjemploAmano extends javax.swing.JFrame {

    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JTextField jTextField1;

    private javax.swing.JLabel pagasLabel;
    private javax.swing.JLabel euroLabel2;
    private javax.swing.JTextField pagasTextField;
    private javax.swing.JLabel edadLabel;
    private javax.swing.JTextField edadTextField;
    private javax.swing.JButton calcularButton;

    private javax.swing.JLabel alMesLabel;
    private javax.swing.JLabel resultadoMesLabel;
    private javax.swing.JLabel euroLabel3;
    private javax.swing.JLabel extraLabel;
    private javax.swing.JLabel resultadoExtraLabel;
    private javax.swing.JLabel euroLabel4;

    public EjemploAmano() {
        //Llamadas a metodos
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();

        pagasLabel = new javax.swing.JLabel();
        euroLabel2 = new javax.swing.JLabel();
        pagasTextField = new javax.swing.JTextField();
        edadLabel = new javax.swing.JLabel();
        edadTextField = new javax.swing.JTextField();
        calcularButton = new javax.swing.JButton();

        alMesLabel = new javax.swing.JLabel();
        resultadoMesLabel = new javax.swing.JLabel();
        euroLabel3 = new javax.swing.JLabel();
        extraLabel = new javax.swing.JLabel();
        resultadoExtraLabel = new javax.swing.JLabel();
        euroLabel4 = new javax.swing.JLabel();

        jLabel1.setText("Calculadora de Sueldo");
        jLabel2.setText("Sueldo bruto anual (lo que ganas al año)");
        jTextField1.setHorizontalAlignment(javax.swing.JTextField.RIGHT);
        jLabel3.setText("€");

        pagasLabel.setText("Número de pagas");
        pagasTextField.setHorizontalAlignment(javax.swing.JTextField.RIGHT);
        euroLabel2.setText("€");
        edadLabel.setText("Edad");
        edadTextField.setHorizontalAlignment(javax.swing.JTextField.RIGHT);

        alMesLabel.setText("Ganarías al mes");
        resultadoMesLabel.setText("0");
        resultadoMesLabel.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        euroLabel3.setText("€");

        extraLabel.setText("Paga extra neta");
        resultadoExtraLabel.setText("0");
        resultadoExtraLabel.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        euroLabel4.setText("€");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        calcularButton.setText("Calcular");
        calcularButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                calcularButtonActionPerformed(evt);
            }
        });
        
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);

        //control horizontal
        layout.setHorizontalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createSequentialGroup()
                                .addGap(16, 16, 16)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                        .addComponent(jLabel1)
                                        .addGroup(layout.createSequentialGroup()
                                                .addGap(6, 6, 6)
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                        .addComponent(jLabel2)
                                                        .addGroup(layout.createSequentialGroup()
                                                                .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                                                .addComponent(jLabel3))))
                                        .addGroup(layout.createSequentialGroup()
                                                .addGap(6, 6, 6)
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                        .addComponent(pagasLabel)
                                                        .addGroup(layout.createSequentialGroup()
                                                                .addComponent(pagasTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                                                .addComponent(euroLabel2)
                                                                .addComponent(euroLabel3)
                                                                .addComponent(euroLabel4))))
                                        .addGroup(layout.createSequentialGroup()
                                                .addGap(6, 6, 6)
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                        .addComponent(edadLabel)
                                                        .addComponent(edadTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                        .addComponent(alMesLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                        .addComponent(resultadoMesLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                        .addComponent(extraLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                        .addComponent(resultadoExtraLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                        .addComponent(calcularButton, javax.swing.GroupLayout.PREFERRED_SIZE, 101, javax.swing.GroupLayout.PREFERRED_SIZE))
                                                .addContainerGap(250, Short.MAX_VALUE))))
        );

        //control vertical
        layout.setVerticalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createSequentialGroup()
                                .addGap(16, 16, 16)
                                .addComponent(jLabel1)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jLabel2)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addComponent(jLabel3))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(pagasLabel)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(pagasTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addComponent(euroLabel2))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(edadLabel)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(edadTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(calcularButton)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(alMesLabel)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(resultadoMesLabel)
                                        .addComponent(euroLabel3))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(extraLabel)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(resultadoExtraLabel)
                                        .addComponent(euroLabel4))
                                .addContainerGap(250, Short.MAX_VALUE))
        );

        pack();
    }

    private void calcularButtonActionPerformed(java.awt.event.ActionEvent evt) {
        System.out.println("Has pulsado el botón");
        resolver(jTextField1, pagasTextField, edadTextField, resultadoMesLabel, resultadoExtraLabel);
    }

    private void resolver(JTextField salario, JTextField pagas, JTextField edad, JLabel eurosMes, JLabel extraNeta) {

        String campoSalario = salario.getText(); 
        String campoPagas = pagas.getText(); 
        String campoEdad = edad.getText();  
        
        try{
        float gananciaMensual;
        float redondeoPagaExtra;
        float redondeoGananciaMensual;
        float redondeoGmensualConImp;
        float mensualSS=0;
        float mensualIrpf=0;
        float gananciaMesConImp;
        String resultadoAlMes;
        String resultadoPagaExtra;

        float salarioFloat = Float.parseFloat(campoSalario);
        float pagasInt = Integer.parseInt(campoPagas);
        int edadInt = Integer.parseInt(campoEdad);

        gananciaMensual = salarioFloat / pagasInt;
        redondeoPagaExtra = Math.round(gananciaMensual * 100.0f) / 100.0f;
        redondeoGananciaMensual = Math.round(gananciaMensual * 100.0f) / 100.0f;
        System.out.println(gananciaMensual);

        //rangos de edad SS
        if (edadInt<23 || edadInt>=60) {
            mensualSS = redondeoGananciaMensual*0.02f;
        }else if (edadInt>=23 && edadInt<60) {
            mensualSS = redondeoGananciaMensual*0.056f;
        }
        //rangos de sueldo irpf
        if (salarioFloat<16000) {
            mensualIrpf = redondeoGananciaMensual*0.02f;
        }else if (salarioFloat>=16000 && salarioFloat<24000) {
            mensualIrpf = redondeoGananciaMensual*0.12f;
        }else if (salarioFloat>=24000 && salarioFloat<36000) {
            mensualIrpf = redondeoGananciaMensual*0.18f;
        }else if (salarioFloat>=36000 && salarioFloat<200000) {
            mensualIrpf = redondeoGananciaMensual*0.25f;
        }else if (salarioFloat>=200000 && salarioFloat<Float.MAX_VALUE) {
            mensualIrpf = redondeoGananciaMensual*0.40f;
        }
        //ganancia al mes con impuestos
        gananciaMesConImp = redondeoGananciaMensual-mensualSS-mensualIrpf;
        redondeoGmensualConImp = Math.round(gananciaMesConImp * 100.0f) / 100.0f;
        resultadoAlMes = String.valueOf(redondeoGmensualConImp);
        eurosMes.setText(resultadoAlMes);
        //paga extra neta
        if (pagasInt<=12) {
            extraNeta.setText("0");
        }else if (pagasInt>12) {
            resultadoPagaExtra = String.valueOf(redondeoPagaExtra);
            extraNeta.setText(resultadoPagaExtra);
        }
        
        //Limpiar campos
        salario.setText("");
        pagas.setText("");
        edad.setText("");
        
         }catch(Exception e){
        System.out.println(e.getMessage());
        }

    }

    public static void main(String[] args) {

        //Esto mantiene la ventana inicial corriendo hasta que la cerremos
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new EjemploAmano().setVisible(true);
            }
        });

    }

}

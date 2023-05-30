import javax.crypto.*;
import java.io.*;
import java.security.*;
import java.util.*;



class practical3
{
    public static void main(String args[]) throws Exception
    {
       
        String target = "This Is Confidential Message";
        byte[] mymessage = target.getBytes();
        

        //generate key

        KeyGenerator newkey = KeyGenerator.getInstance("DES");
        SecretKey s = newkey.generateKey();


        //ciper
        Cipher c = Cipher.getInstance("DES");
        c.init(Cipher.ENCRYPT_MODE, s);
        byte[] encryptedmsg = c.doFinal(mymessage);

        //decrypt

        c.init(c.DECRYPT_MODE, s);
        byte[] decrypted = c.doFinal(encryptedmsg);

        String  enc = new String(encryptedmsg);
        String  dec = new String(decrypted);
        System.out.println("encrypted data is" + enc);
        System.out.println("Decrupted data is" + dec);


    }
}
import java.math.BigInteger;

public class practical8 {

    public static void main(String[] args) {
        // Step 1: Generate two distinct prime numbers
        BigInteger p = new BigInteger("17"); // First prime number
        BigInteger q = new BigInteger("11"); // Second prime number

        // Step 2: Compute modulus (n) by multiplying p and q
        BigInteger modulus = p.multiply(q);

        // Step 3: Compute Euler's totient function (phi) for modulus
        BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));

        // Step 4: Choose a public key (e) that is relatively prime to phi
        BigInteger publicKey = new BigInteger("7");

        // Step 5: Compute the modular multiplicative inverse (d) of public key
        BigInteger privateKey = publicKey.modInverse(phi);

        // Message to be encrypted and decrypted
        BigInteger message = new BigInteger("8");

        // Step 6: Encrypt the message using the public key
        BigInteger encryptedMessage = message.modPow(publicKey, modulus);

        // Step 7: Decrypt the encrypted message using the private key
        BigInteger decryptedMessage = encryptedMessage.modPow(privateKey, modulus);

        // Print the results
        System.out.println("Original Message: " + message);
        System.out.println("Encrypted Message: " + encryptedMessage);
        System.out.println("Decrypted Message: " + decryptedMessage);
    }
}

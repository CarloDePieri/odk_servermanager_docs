��          �               �   g   �   L   e  =  �  �   �  Z   �  b   �  Q   [     �  �   �  e   G     �  �   �  �   T  |    j   �  Z   �  ^  P	  �   �
  }   p  c   �  U   R     �  �   �  n   I     �  �   �    x   :option:`instances_root <bootstrap instances_root>`: the directory in which the instances will be saved :option:`odksm_folder_path <bootstrap odksm_folder_path>`: the root of ODKSM Additional fields can be set in ``bootstrap.ini``: these will be default values in newly created instances' ``config.ini``, so it makes sense to set them here only if they are global values for the whole server, like maybe :option:`arma_folder <ODKSM arma_folder>` or :option:`password_admin <config password_admin>`. Begin with choosing a folder that will be the root of all server instances. Copy there both ``START.bat`` and ``bootstrap.ini``, that can be found in the ODKSM root folder. Finally, edit ``START.bat`` and set the variable ``ODKSM_FOLDER_PATH`` to your ODKSM root. First of all, make sure that ODKSM is installed and that you know how to configure a new instance. Now edit ``bootstrap.ini`` and set the two fields in the ``[bootstrap]`` section: Quick Start Tool Simply launch the ``START.bat`` script. A console ui will ask for the instance name and whether to include :doc:`templates <templates>`. This tool aims to automate all actions taken at the very beginning of a new server instance creation. Usage When keeping ``bootstrap.ini`` and ``START.bat`` in different folders, edit the latter and set the variable ``DEFAULT_CONFIG`` to the path of ``bootstrap.ini``. You are **not** done! The tool just created a new folder, where it put everything needed to start configuring the server instance as explained in :ref:`usage:Create a server instance`. Project-Id-Version: odksm_docs 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2020-05-17 10:11+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: it
Language-Team: it <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.8.0
 :option:`instances_root <bootstrap instances_root>`: la cartella in cui le istanze server verranno salvate :option:`odksm_folder_path <bootstrap odksm_folder_path>`: la cartella principale di ODKSM Dentro ``bootstrap.ini`` possono essere settati molti altri campi: questi saranno impostati come valori di default nelle nuove istanze create dal tool, quindi ha senso settarli qui soltanto nel caso siano valori globali per l'intero server, come ad esempio :option:`arma_folder <ODKSM arma_folder>` o :option:`password_admin <config password_admin>`. Iniziare scegliendo la cartella che conterrà tutte le istanze server create. Copiare lì ``START.bat`` e ``bootstrap.ini``: entrambi possono essere trovati nella cartella principale di ODKSM. Infine, aprire ``START.bat`` e inserire il percorso della cartella principale di ODKSM nella variabile ``ODKSM_FOLDER_PATH``. Prima di tutto, accertarsi che ODKSM sia installato e di sapere come configurare una nuova istanza. Ora aprire ``bootstrap.ini`` e settare qui i due campi nella sezione ``[bootstrap]``: Tool di Quick Start Lanciare lo script ``START.bat``. Una interfaccia da console chiederà il nome dell'istanza e se includere dei :doc:`templates <templates>`. Questo tool mira ad automatizzare le azioni necessarie all'inizio della creazione di una nuova istanza server. Utilizzo Nel caso ``bootstrap.ini`` e ``START.bat`` vengano tenuti in due cartelle diverse, aprire quest'ultimo e impostare la variabile ``DEFAULT_CONFIG`` sul percorso del ``bootstrap.ini``. Questo **non** è sufficiente per far partire l'istanza! Il tool ha soltanto creato la nuova cartella, dove ha generato tutto il necessario per iniziare la configurazione di una nuova istanza server come spiegato in :ref:`Creare una istanza server <usage:Create a server instance>`. 